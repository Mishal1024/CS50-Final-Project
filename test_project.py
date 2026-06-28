import project
import pytest


tasks = []

def test_add_task():
    project.add_task("task","priority",tasks)
    assert tasks[-1].task == "task" and tasks[-1].priority == "priority" and tasks[-1].done == "Incomplete"

def test_mark_task():
    project.mark_task(0,tasks)
    assert tasks[-1].done == "Complete"

def test_unmark_task():
    project.unmark_task(0,tasks)
    assert tasks[-1].done == "Incomplete"


habits = []

def test_add_habit():
    project.add_habit("habit1","frequency1","target1",habits)
    assert habits[-1].habit == "habit1" and habits[-1].frequency == "frequency1" and habits[-1].target == "target1"

def test_remove_habit():
    project.add_habit("habit2","frequency2","target2",habits)
    project.remove_habit(0,habits)
    assert habits[-1].habit != "habit2"


notes = []

def test_add_note():
    project.add_note("title1","content1",notes)
    assert notes[-1].title == "title1" and notes[-1].content == "content1"

def test_remove_note():
    project.add_note("title1","content2",notes)
    project.remove_note(0,notes)
    assert notes[-1].title != "title2"


logs = []

def test_add_log():
    project.add_log("action","detail",logs)
    assert logs[-1].action == "action" and logs[-1].detail == "detail"
    for i in range(100):
        project.add_log(f"action{i+1}",f"detail{i+1}",logs)
    assert logs[0].action == "action1" and logs[0].detail == "detail1"


def test_int_validation():
    with pytest.raises(ValueError):
        project.int_validation("abc",logs)