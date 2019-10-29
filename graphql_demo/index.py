from graphene import *
from flask_graphql.graphqlview import GraphQLView
from flask import Flask
from graphql_demo.graphql_schema import MyQuery

app = Flask(__name__)


schema = Schema(query=MyQuery, auto_camelcase=False)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
