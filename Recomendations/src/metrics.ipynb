{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "conda install -c conda-forge implicit\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import implicit\n",
    "%matplotlib inline\n",
    "\n",
    "# Для работы с матрицами\n",
    "from scipy.sparse import csr_matrix, coo_matrix\n",
    "\n",
    "# Детерминированные алгоритмы\n",
    "from implicit.nearest_neighbours import ItemItemRecommender, CosineRecommender, TFIDFRecommender, BM25Recommender\n",
    "\n",
    "# Метрики\n",
    "from implicit.evaluation import train_test_split\n",
    "from implicit.evaluation import precision_at_k, mean_average_precision_at_k, AUC_at_k, ndcg_at_k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def weighted_random_recommendation_2(data, n=5):\n",
    "    \"\"\"Случайные рекоммендации\n",
    "    \n",
    "\n",
    "    Input\n",
    "    -----\n",
    "    items_weights: pd.DataFrame\n",
    "        Датафрейм со столбцами item_id, weight. Сумма weight по всем товарам = 1\n",
    "    \"\"\"\n",
    "    \n",
    "    # Подсказка: необходимо модифицировать функцию random_recommendation()\n",
    "    # your_code\n",
    "    sw = int(np.log(data['sales_value'].sum()))\n",
    "    popularity = data.groupby('item_id')['sales_value'].sum().reset_index()\n",
    "    popularity['weight'] = np.log(popularity['sales_value'])/sw\n",
    "    \n",
    "    \n",
    "    popularity.sort_values('weight', ascending=False, inplace=True)\n",
    "    \n",
    "    recs = popularity.head(n).item_id\n",
    "    \n",
    "    return recs.tolist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def hit_rate(recommended_list, bought_list):\n",
    "    \n",
    "    bought_list = np.array(bought_list)\n",
    "    recommended_list = np.array(recommended_list)\n",
    "    \n",
    "    flags = np.isin(bought_list, recommended_list)\n",
    "    \n",
    "    hit_rate = (flags.sum() > 0) * 1\n",
    "    \n",
    "    return hit_rate\n",
    "\n",
    "\n",
    "def hit_rate_at_k(recommended_list, bought_list, k=5):\n",
    "    \n",
    "    # your_code\n",
    "    \n",
    "    return hit_rate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def precision(recommended_list, bought_list):\n",
    "    \n",
    "    bought_list = np.array(bought_list)\n",
    "    recommended_list = np.array(recommended_list)\n",
    "    \n",
    "    flags = np.isin(bought_list, recommended_list)  # [False, False, True, True]\n",
    "    \n",
    "    precision = flags.sum() / len(recommended_list)\n",
    "    \n",
    "    return precision\n",
    "\n",
    "\n",
    "def precision_at_k(recommended_list, bought_list, k=5):\n",
    "    \n",
    "    bought_list = np.array(bought_list)\n",
    "    recommended_list = np.array(recommended_list)\n",
    "    \n",
    "    bought_list = bought_list  # Тут нет [:k] !!\n",
    "    recommended_list = recommlist[:k]\n",
    "    \n",
    "    flags = np.isin(bought_list, recommended_list)\n",
    "    \n",
    "    precision = flags.sum() / len(recommended_list)\n",
    "    \n",
    "    return precision"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def recall(recommended_list, bought_list):\n",
    "    \n",
    "    bought_list = np.array(bought_list)\n",
    "    recommended_list = np.array(recommended_list)\n",
    "    \n",
    "    flags = np.isin(bought_list, recommended_list)  # [False, False, True, True]\n",
    "    \n",
    "    recall = flags.sum() / len(bought_list)\n",
    "    \n",
    "    return recall"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def recall_at_k(recommended_list, bought_list, k=5):\n",
    "    \n",
    "    bought_list = np.array(bought_list)\n",
    "    recommended_list = np.array(recommended_list)\n",
    "    \n",
    "    flags = np.isin(bought_list, recommended_list)  # [False, False, True, True]\n",
    "    \n",
    "    recall = flags.sum() / len(bought_list)\n",
    "    \n",
    "    return recall"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
