# Controller/DashboardController.py
from flask import Flask, render_template
from src.interface.ObController import ObController


class DashboardController(ObController):

    def register(self):
        self._app.add_url_rule('/dashboard', 'dashboard',
                               self._auth(self.dashboard), methods=['GET'])

    def dashboard(self):
        signages = self._model_store.node_player().get_signages()
        return self.render_view(
            '@dashboard.jinja.html',
            count_players=len(signages),
            signages=signages
        )
