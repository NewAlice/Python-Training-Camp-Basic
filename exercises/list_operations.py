"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    if operation == "add":
        for s in args:
            students.append(s)
        return students
    elif operation == "update":
        for i, s in enumerate(students):
            if s == args[0]:
                students[i] = args[1]
                break
        return students
    elif operation == "remove":
        index = -1
        for i, s in enumerate(students):
            if s == args[0]:
                index = i
                break
        if index != -1:
            if index == len(students) - 1:
                return students[:index]
            elif index == 0:
                return students[1:]
            return students[:index] + students[index+1:]
