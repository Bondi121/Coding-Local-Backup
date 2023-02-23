def print_teacher (**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_teacher(name='Ashley', job='Instructor', topic='Python', second_topic='javascript')


teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}

def print_teachers(name, job, topic):
    print(name)
    print(job)
    print(topic)

print_teachers(**teacher)
