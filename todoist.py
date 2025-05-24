from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Task


api = TodoistAPI('d0dce30cb3c7bbf525d500dfd9943d5f36b222bf')
task = api.get_task('6XpMw63VFchwPHMw')
print(f'Task: {task.content}')

api.update_task('6XpMw63VFchwPHMw', content='Begynd på space cowboy 🥹')
proj = api.get_project('6CrfF3Cjjr4F6g9w')
task_list = api.get_tasks(project_id='6CrfF3Cjjr4F6g9w')

for tasks in task_list:
    for task in tasks:
        print(task.content)

# Creating a task
task_test = Task(
    id='1',
    content='test',
    description='a test task',
    project_id='2',
    section_id='3',
    parent_id='4',
    labels=['a', 'n'],
    priority=1,
    due=None,
    deadline=None,
    duration=None,
    is_collapsed=None,
    order=None,
    assignee_id=None,
    assigner_id=None,
    completed_at=None,
    creator_id=None,
    created_at=None,
    updated_at=None,
    meta=None
)

print(task_test)
# comments_iter = api.get_comments(task_id=task.id)
# for comments in comments_iter:
#     for comment in comments:
#         print(f'Comment: {comment.content}')