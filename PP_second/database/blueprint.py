from flask import Blueprint, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

import db_utils
from models import * 
from schemas import * 

api_blueprint = Blueprint("api", __name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_passsword(username,password):
    session = Session()
    user = session.query(Users).filter_by(email = username).one()
    if check_password_hash(user.password,password):
        return user


@api_blueprint.route("/users", methods=["POST"])
def create_users():
    users_data = UsersToCreate().load(request.json)
    user = db_utils.create_entry(Users, **users_data)
    return jsonify(UsersData().dump(user)), 200

@api_blueprint.route("/users/<int:id>", methods = ["PUT"])
#@auth.login_required
def update_users(id):
    session = Session()
    user = auth.current_user()
    users_data = UsersToUpdate().load(request.json)
    ori_users_data = session.query(Users).filter_by(id = id).one()
    if user.id != ori_users_data.id:
            return (jsonify({"code": 400, "error": "You aren`t owner"}))
    for key , value in users_data.items():
        setattr(ori_users_data,key,value)
    session.commit()
    return jsonify(UsersData().dump(ori_users_data)),200




@api_blueprint.route("/users/<int:id>", methods=["GET"])
def get_users_by_id(id):
    users = db_utils.get_entry_by_id(Users, id)
    return jsonify(UsersData().dump(users))

@api_blueprint.route("/users/<int:id>", methods=["DELETE"])
@auth.login_required
def delete_users(id):
    session = Session()
    user = auth.current_user()
    if session.query(Users).filter_by(id=id).first() == None:
        return(jsonify({"code": 404 ,"error": "Wrong id"})),404
    if user.id != id:
        return (jsonify({"code": 403,"error": "You aren`t owner"})),403
    db_utils.delete_entry(Users, id)
    return jsonify(StatusResponse().dump({"code": 200}))



@api_blueprint.route("/article", methods=["POST"])
#@auth.login_required
def create_article():
    article_data = ArticleToCreate().load(request.json)
    article = db_utils.create_entry(Articles, **article_data)
    return jsonify(ArticleData().dump(article)),200




@api_blueprint.route("/article/<int:aid>", methods = ["PUT"])
@auth.login_required
def update_article(aid):
    session = Session()
    user = auth.current_user()
    article_data = ArticleToUpdate().load(request.json)
    ori_article_data = session.query(Articles).filter_by(aid = aid).one()
    for key , value in article_data.items():
        setattr(ori_article_data,key,value)
    a = "waiting for admitting"
    session.query(Articles).filter_by(aid = aid).update({"status": a})
    session.commit()
    return jsonify(ArticleData().dump(ori_article_data)),200

@api_blueprint.route("/article_confirm/<int:aid>", methods = ["PUT"])
@auth.login_required
def confirm_article(aid):
    session = Session()
    user = auth.current_user()
    if user.ustatus != "moderator":
            return (jsonify({"code": 400, "error": "You aren`t moderator"}))
    article_data = ArticleToConfirm().load(request.json)
    ori_article_data = session.query(Articles).filter_by(aid = aid).one()
    for key , value in article_data.items():
        setattr(ori_article_data,key,value)
    a = "admitted"
    session.query(Articles).filter_by(aid = aid).update({"status": a})
    session.commit()
    return jsonify(ArticleData().dump(ori_article_data)),200


@api_blueprint.route("/article/<int:aid>", methods=["GET"])
@auth.login_required
def get_article_by_id(aid):
    article = db_utils.get_entry_by_aid(Articles, aid)
    if session.query(Articles).filter_by(aid = aid).first() == None:
        return (jsonify({"code": 404, "error": "Wrong id"})), 404
    return jsonify(ArticleData().dump(article)),200

@api_blueprint.route("/article/<int:aid>", methods=["DELETE"])
@auth.login_required
def delete_article(aid):
    session = Session()
    user = auth.current_user()
    if user.id != aid:
            return (jsonify({"code": 403, "error": "You aren`t owner"}))
    if session.query(Articles).filter_by(aid=aid).first() == None:
        return(jsonify({"code": 404 ,"error": "Wrong id"})),404
    db_utils.delete_entrya(Articles, aid)
    return jsonify(StatusResponse().dump({"code": 200}))

@api_blueprint.route("/article", methods=["GET"])
def list_articles():
    session = Session()
    article = session.query(Articles).all()
    return jsonify(ArticleData(many=True).dump(article))














