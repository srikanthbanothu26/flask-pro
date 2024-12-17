from flask import Blueprint,render_template

route_bp=Blueprint("routes",__name__)
@route_bp.route('/', methods=["GET","POST"])
def home():
    return render_template("home.html")


@route_bp.route('/scroll', methods=['GET','POST'])
def view():
    return render_template("scroll.html")


@route_bp.route('/add_recipie',methods=["GET","POST"])
def addrecipie():
    return render_template("add_recipie.html")


