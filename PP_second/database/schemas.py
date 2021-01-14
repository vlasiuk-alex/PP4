from marshmallow import validate, Schema, fields, post_load

class UsersData(Schema):
    id = fields.Integer()
    username = fields.String()
    firstname = fields.String()
    lastname = fields.String()
    email = fields.String(validate=validate.Email())
    ustatus = fields.String()

class UsersToCreate(Schema):
    username = fields.String(required=True)
    firstname = fields.String()
    lastname = fields.String()
    email = fields.String(validate=validate.Email())
    password = fields.String()
    ustatus = fields.String()

class UsersToUpdate(Schema):
    username = fields.String()
    firstname = fields.String()
    lastname = fields.String()
    email = fields.String(validate=validate.Email())
    password = fields.String()
    ustatus = fields.String()

class ListUsersRequest(Schema):
    username = fields.String()
    firstname = fields.String()
    lastname = fields.String()
    email = fields.String(validate=validate.Email())
    ustatus = fields.String()

class ArticleData(Schema):
    aid = fields.Integer()
    title = fields.String()
    text = fields.String()
    date = fields.String()
    status = fields.String()

class ArticleToCreate(Schema):
    title = fields.String()
    text = fields.String()
    date = fields.String()
    status = fields.String()

class ArticleToUpdate(Schema):
    title = fields.String()
    text = fields.String()
    date = fields.String()
    status = fields.String()
    
class ArticleToConfirm(Schema):
    title = fields.String()
    text = fields.String()
    date = fields.String()
    status = fields.String()

class ListArticlesRequest(Schema):
    title = fields.String()
    text = fields.String()
    date = fields.String()
    status = fields.String()

class UarticlesData(Schema):
    art_id = fields.Integer()
    us_id = fields.Integer()
    mod_id = fields.Integer()
    ed_text = fields.String()
    ed_date = fields.String()

class ListUarticlesRequest(Schema):
    art_id = fields.Integer()
    us_id = fields.Integer()
    mod_id = fields.Integer()
    ed_text = fields.String()
    ed_date = fields.String()

class StatusResponse(Schema):
    code = fields.Integer()
    type = fields.String(default="OK")
    message = fields.String(default="OK")










