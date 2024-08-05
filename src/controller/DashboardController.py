import time
import json
import threading

from flask import Flask
import render_template
import redirect
import request
import url_for
import jsonify
from src.interface.ObController import ObController
from src.util.utils import restart
from src.service.ModelStore import ModelStore


class DashboardController(ObController):

    def register(self):
        self._app.add_url_rule('/dashboard', 'dashboard_index',
                               self.dashboard_index, methods=['GET'])

    def dashboard_index(self):
        self._model_store.variable().update_by_name(
            'last_pillmenu_dashboard', 'dashboard_index')

        return render_template('dashboard/index.jinja.html')
