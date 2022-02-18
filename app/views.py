from flask import Blueprint, render_template, request
from app.scrapping import scrap_from_url
from app.database import add_scrap_to_db, delete_scrap_from_db, show_scrap, show_all_scrap, delete_all_scrap
views = Blueprint('views', __name__)

@views.route('/',methods=['POST','GET'])
def main():
    if request.method == 'POST':
        url = request.form.get('URL_scrap')
        add_scrap = request.form.get('add_scrap')
        id_to_delete = request.form.get('id_to_delete')
        id_to_show = request.form.get('id_to_show')
        show_all = request.form.get('show_all')
        delete_all = request.form.get('delete_all')

        if add_scrap:
            dictionnaire=scrap_from_url(url)
            id_scrap=add_scrap_to_db(dictionnaire,url)
            return render_template("views/main.html",url=url,dictionnaire=dictionnaire,id_scrap=id_scrap)

        if id_to_delete:
            delete_scrap_from_db(id_to_delete)
            return render_template("views/main.html",id_to_delete=id_to_delete)
        
        if delete_all:
            DB_stat=delete_all_scrap()
            return render_template("views/main.html",DB_stat=DB_stat)         

        if id_to_show:
            scrap=show_scrap(id_to_show)
            return render_template("views/main.html",id_to_show=id_to_show,dictionnaire=scrap[0],url=scrap[1]) 
            
        if show_all:
            scraps=show_all_scrap()
            return render_template("views/main.html",scraps=scraps) 
        
    return render_template("views/main.html")
