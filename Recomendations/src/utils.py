{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def prefilter_items(data, take_n_popular=5000):\n",
    "    \"\"\"Предфильтрация товаров\"\"\"\n",
    "    \n",
    "    # 1. Удаление товаров, со средней ценой < 1$\n",
    "    # your_code\n",
    "    data['price'] = data['sales_value'] / (np.maximum(data['quantity'], 1))\n",
    "    data = data[data['price'] > 1]\n",
    "    \n",
    "    \n",
    "    \n",
    "    # 2. Удаление товаров со соедней ценой > 30$\n",
    "    # your_code\n",
    "    data = data[data['price'] <= 30]\n",
    "    \n",
    "    # 3. Придумайте свой фильтр (убираем товары по скидке которые и так продвигаются)\n",
    "    # your_code\n",
    "    data = data[data['retail_disc'] > -0.3]\n",
    "    \n",
    "    # 4. Выбор топ-N самых популярных товаров (N = take_n_popular)\n",
    "    # your_code\n",
    "    \n",
    "    popularity = data.groupby('item_id')['quantity'].sum().reset_index()\n",
    "    top = popularity.sort_values('quantity', ascending=False).head(take_n_popular).item_id.tolist()\n",
    "    \n",
    "\n",
    "    \n",
    "    \n",
    "    return top"
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
