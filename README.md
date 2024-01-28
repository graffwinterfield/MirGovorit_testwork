# Service

# install python3.8
<pre>
sudo apt update
sudo apt install python3
</pre>

# download project
<pre>
git clone https://github.com/graffwinterfield/MirGovorit_testwork.git
cd MirGovorit/
pip install -r requirments.txt
</pre>
# start
<pre>
python3 manage.py runserver 0.0.0.0:8000
</pre>


# usage
<pre>
Админка http://127.0.0.1:8000/admin/
user: graff
pass: 4774

Функционал:
http://127.0.0.1:8000/home/add_product_to_recipe/?recipe_id=1&product_id=1&weight=300 #добавляет в рецепт продукты
http://127.0.0.1:8000/home/cook_recipe/?recipe_id=1 #Увеличивает на единицу кол-во использованных продуктов
http://127.0.0.1:8000/home/show_recipes_without_product/?product_id=3 #рецпеты с фильтром
http://127.0.0.1:8000/home/show_all/?recipe_id=2 #показывает все рецепты и их состав включая вес
</pre>

