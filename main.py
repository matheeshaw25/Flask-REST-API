from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)# wrap our app in an API - RESTFUL

 #serializable format
names = {"tim":{"age":19, "gender":"male"},
         "bill":{"age":55, "gender":"male"}}

class HelloWorld(Resource): #inherit from Resource
    def get(self,name): #GET request
        return names[name]


api.add_resource(HelloWorld,"/helloworld/<string:name>") # register the class HelloWorld as a resource - if we send a GET request to /helloworld , it will return ""Hello World"

if __name__ == "__main__":
    app.run(debug=True)