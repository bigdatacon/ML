import numpy as np


def precision(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def precision_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    

    bought_list = bought_list  # Тут нет [:k] !!
    
    if k < len(recommended_list):
        recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision


def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5):
    # your_code
    # Лучше считать через скалярное произведение, а не цикл

    return precision


def recall(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall


def recall_at_k(recommended_list, bought_list, k=5):

    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    if k < len(recommended_list):
        recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)
    recall = flags.sum() / len(bought_list)

    return recall


def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k=5):
    bought_list = np.array(bought_list)
    prices_bought = np.array(prices_bought)
    recommended_list = np.array(recommended_list)[:k]
    prices_recommended = np.array(prices_recommended)[:k]
    
    prices_all = np.sum(prices_bought)
    
    flags = np.isin(recommended_list, bought_list) 
    prices = np.dot(flags, prices_recommended)
    
    return prices/prices_all 

def money_precision_at_k(recommended_list, bought_list, prices_recommended, k=5):
        
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)[:k]
    prices_recommended = np.array(prices_recommended)[:k]
    
    flags = np.isin(recommended_list, bought_list) 
    prices_all = np.dot(np.ones((k,)), prices_recommended)
    prices = np.dot(flags, prices_recommended)
      
    return prices/prices_all

def postfilter_items(items, items_info, bought, most_popular_items , N=5):
    def get_department(i):
        department = items_info[items_info['item_id'] == i]['department'].values[0]
        return department

    not_cheap_items = items_info[items_info['price'] > 1.0]
    item_ids = pd.DataFrame(items, columns=['item_id'])
    never_bought_items = item_ids[~item_ids['item_id'].isin(bought)]['item_id'].values.tolist()
    expensive_items =  item_ids.merge(items_info[items_info['price']>7], on='item_id', how='right').head(5)['item_id'].values.tolist()
    
    categories_used = []
    final_recommendations = []
    
    
    expensive_item_id = expensive_items[0]
    final_recommendations.append(expensive_item_id)
    categories_used.append(get_department(expensive_item_id))
    
    for i in items:
        if any(not_cheap_items[not_cheap_items['item_id'] == i]['price']):
            if  get_department(i) not in categories_used:
                final_recommendations.append(i)
                categories_used.append( get_department(i))
        if len(final_recommendations) == 3:
            break

    for i in never_bought_items:
        if any(not_cheap_items[not_cheap_items['item_id'] == i]['price']):
            if  get_department(i) not in categories_used:
                final_recommendations.append(i)
                categories_used.append( get_department(i))
        if len(final_recommendations) == 5:
            break
            
    for i in most_popular_items:
        if any(not_cheap_items[not_cheap_items['item_id'] == i]['price']):
            if  get_department(i) not in categories_used:
                final_recommendations.append(i)
                categories_used.append( get_department(i))
        if len(final_recommendations) == 5:
            break            
        
    assert len(final_recommendations) == N, 'Количество рекомендаций = {}, должно быть {}'.format(len(final_recommendations), N)
    assert len(categories_used) == len(set(categories_used)), '{} уникальных категорий'.format(len(set(categories_used)))
    return final_recommendations

###  Для инфо как вызывается prefilter_items:
# postfilter_items(recommendations, item_info=item_features, N=5)


# Финальный проект
# Мы уже прошли всю необходимую теорию для финального проекта. Проект осуществляется на данных из вебинара (данные считаны в начале ДЗ). Рекомендуем вам начать делать проект сразу после этого домашнего задания

# Целевая метрика - money precision@5. Порог для уcпешной сдачи проекта money precision@5 > 20%
# Бизнес ограничения в топ-5 товарах:

# Для каждого юзера 5 рекомендаций (иногда модели могут возвращать < 5)

# 2 новых товара (юзер никогда не покупал)

# 1 дорогой товар, > 7 долларов

# Все товары из разных категорий (категория - department)

# Стоимость каждого рекомендованного товара > 1 доллара

# Будет public тестовый датасет, на котором вы сможете измерять метрику

# Также будет private тестовый датасет для измерения финального качества

# НЕ обязательно использовать 2-ух уровневые рекоммендательные системы в проекте

# Вы сдаете код проекта в виде github репозитория и .csv файл с рекомендациями. В .csv файле 2 столбца: user_id - (item_id1, item_id2, ..., item_id5)