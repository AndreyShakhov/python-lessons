# получаем количкство запросов
num_req = int(input('введите кол-во запросов от 1 до 100    '))
print(num_req)
tree_space = {}  # дерево пространств
# набор пространств и переменных
parent = None


def space_var(key, space):
    if key in tree_space:
        list_space = [tree_space.get(key), space]
        tree_space.pop(key)
        tree_space[key] = list_space
    else:
        tree_space[key] = space


def create_namespace(parent_namespace, children_namespace):
    if parent_namespace in tree_space:
        tree_space[parent_namespace].append(children_namespace)
        tree_space[children_namespace] = []
    else:
        tree_space['global'] = [parent_namespace]
        tree_space[parent_namespace] = [children_namespace]
        tree_space[children_namespace] = []


def add_variable(namespace, variable):
    if namespace in tree_space:
        tree_space[namespace].append(variable)
    else:
        create_namespace("global", namespace)
        tree_space[namespace] = [variable]


def get_variable(variable_name, namespace) -> str:
    if namespace in tree_space:
        for item in tree_space[namespace]:
            if variable_name == item:
                return namespace

        if namespace == 'global':
            return None
        for key in tree_space.keys():
            for item in tree_space[key]:
                if item == namespace:
                    return get_variable(variable_name, key)

    return None


def tree():  # создание дерева и поиск по дереву
    req = str(input('введите запрос  '))
    req_list = req.split()
    if req_list[0] == 'create':
        children_namespace = req_list[1]
        parent_namespace = req_list[2]  # получение имени родителя
        create_namespace(parent_namespace, children_namespace)# вызов функции добавления пространства, переменной в дерево

    if req_list[0] == 'add':  # Проверка - является ли запрос - на создание переменной
        namespace = req_list[1]  # получение имени родительского пространства пространства
        variable = req_list[2]  # получение имени переменной
        add_variable(namespace, variable)# вызов функции добавления пространства, переменной в дерево

    if req_list[0] == 'get':
        namespace = req_list[1]  # получение имени пространства инициализировшего запрос
        variable_name = req_list[2]  # получение имени запрошенной переменной
        result = get_variable(variable_name, namespace)
        itog_rezault.append(result)

itog_rezault = []
n = 0
while n < num_req:
    tree()
    n = n + 1
for element in itog_rezault:
    print(element)






