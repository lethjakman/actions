from actions.actions import Actions
import pytest
import json
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


# Use our actions_test database as created in our setup_test_db.py script
connection_string = os.environ.get("TEST_DB_CONN", "dbname=actions_test")
conn = psycopg2.connect(connection_string)
cur = conn.cursor()

# Create the actions table in our test database
# I didn't include creation for a production model because that belongs in a
# migration system
def setup_module():
    cur.execute("""CREATE TABLE IF NOT EXISTS  actions (
      action text,
      time int
    )"""
    )


# Drop actions so it is created as designated above
def teardown_module():
    cur.execute("drop table actions")
    cur.close()
    conn.close()

# Make sure actions is clean every time we test it
def setup_function(method):
    cur.execute("truncate actions")

# Test adding a single action
def test_add_jump_action():
    input1 = {"action": "jump", "time": 100}
    input1_json = json.dumps(input1)

    actions = Actions(conn)
    actions.add_action(input1_json)
    cur.execute("select count(*) from actions")
    result = cur.fetchone()
    count = result[0]
    assert count == 1

# Test adding multiple to make sure the class can handle multiple executions
def test_add_multiple_actions():
    input1 = {"action": "jump", "time": 100}
    input1_json = json.dumps(input1)
    input2 = {"action": "run", "time": 75}
    input2_json = json.dumps(input2)

    actions = Actions(conn)
    actions.add_action(input1_json)
    actions.add_action(input2_json)

    cur.execute("select count(*) from actions")
    result = cur.fetchone()
    count = result[0]
    assert count == 2

# Test adding a single action
def test_invalid_json_action():
    input1 = {"act": "jump", "time": 100}
    input1_json = json.dumps(input1)

    actions = Actions(conn)

    with pytest.raises(KeyError):
        actions.add_action(input1_json)

# Grab the stats and check averages to make sure it's correct
def test_get_stats():
    input1 = {"action": "jump", "time": 100}
    input1_json = json.dumps(input1)
    input2 = {"action": "run", "time": 75}
    input2_json = json.dumps(input2)
    input3 = {"action": "jump", "time": 200}
    input3_json = json.dumps(input3)

    actions = Actions(conn)
    actions.add_action(input1_json)
    actions.add_action(input2_json)
    actions.add_action(input3_json)

    results_json = actions.get_stats()
    results = json.loads(results_json)

    jump_dict = list(filter(lambda dict: dict["action"] == "jump", results))[0]
    run_dict = list(filter(lambda dict: dict["action"] == "run", results))[0]

    assert jump_dict["avg"] == 150
    assert run_dict["avg"] == 75



