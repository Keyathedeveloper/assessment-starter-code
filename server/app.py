from flask import request, make_response
from config import app, db, api
from models import Project
from flask_restful import Resource

import ipdb

class ProjectList(Resource):
    def get(self):
        projects = Project.query.all()
        return [project.to_dict() for project in projects], 200

class ProjectResource(Resource):

    def find_project(self, id):
        return Project.query.get(id)

    def patch(self, id):
        project = self.find_project(id)

        if not project:
            return {"error": "Invalid request"}, 404

            if 'name' in data:
                project.name = data ['name']
            if 'about' in data:
                project.about = data ['about']
            if 'phase' in data:
                project.phase = data ['phase']
            if 'link' in data:
                project.link = data ['link']
            if 'image' in data:
                project.image = data ['image']

            db.session.commit()

            project = self.find_project(id)
            return project.to_dict()
