def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    rolesTree = {}
    categories = []

    for categoryId in mapping['categoryIdsSorted']:
        categoryValue = mapping['categories'][categoryId]
        roles = []

        for roleId in categoryValue['roleIds']:
            role = {"id": roleId, "text": mapping['roles'][roleId]['name']}
            roles.append(role)

        category = {"id": f'category-{categoryId}', "text": categoryValue['name'], "items": roles}
        categories.append(category)

    rolesTree['categories'] = categories

    return rolesTree
