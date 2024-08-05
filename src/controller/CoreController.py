
from flask import Flask, send_file, render_template_string, jsonify

from src.interface.ObController import ObController


class CoreController(ObController):

    def register(self):
        self._app.add_url_rule('/manifest.json', 'manifest', self.manifest, methods=['GET'])
        self._app.add_url_rule('/favicon.ico', 'favicon', self.favicon, methods=['GET'])

    def manifest(self):
<<<<<<< HEAD
        with open("{}/manifest.jinja.json".format(self.get_template_dir()), 'r') as file:
=======
        with open("{}/manifest.jinja.json".format(self.get_template_folder()), 'r') as file:
>>>>>>> bd6c1b822b23f8ff3dfff57f0466b3d3c27dab24
            template_content = file.read()

        rendered_content = render_template_string(template_content)

        return self._app.response_class(rendered_content, mimetype='application/json')

    def favicon(self):
<<<<<<< HEAD
        return send_file("{}/favicon.ico".format(self.get_web_dir()), mimetype='image/x-icon')
=======
        return send_file("{}/favicon.ico".format(self.get_web_folder()), mimetype='image/x-icon')
>>>>>>> bd6c1b822b23f8ff3dfff57f0466b3d3c27dab24
