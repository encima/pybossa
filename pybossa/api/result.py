# -*- coding: utf8 -*-
# This file is part of PYBOSSA.
#
# Copyright (C) 2015 Scifabric LTD.
#
# PYBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PYBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PYBOSSA.  If not, see <http://www.gnu.org/licenses/>.
"""
PYBOSSA api module for exposing domain object Result via an API.

This package adds GET, POST, PUT and DELETE methods for:
    * tasks

"""
from werkzeug.exceptions import BadRequest
from pybossa.model.result import Result
from api_base import APIBase

from flasgger.utils import swag_from

class ResultAPI(APIBase):

    """Class for domain object Result."""

    __class__ = Result
    reserved_keys = set(['id', 'created', 'project_id',
                         'task_id', 'task_run_ids', 'last_version'])

    @swag_from('swagger/result/GET.yml')
    def get(self, oid):
        return APIBase.get(self, oid)
    
    @swag_from('swagger/result/PUT.yml')
    def put(self, oid):
        return APIBase.put(self, oid)

    @swag_from('swagger/result/POST.yml')
    def post(self):
        return APIBase.post(self)

    @swag_from('swagger/result/DELETE.yml')
    def delete(self, oid):
        return APIBase.delete(self, oid)

    def _forbidden_attributes(self, data):
        for key in data.keys():
            if key in self.reserved_keys:
                raise BadRequest("Reserved keys in payload")
