"""
Copyright (c) 2018 Versentiedge LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS-IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from __future__ import absolute_import
from __future__ import division       # python 2/3 compatibility
from __future__ import print_function # python 2/3 compatibility

# NOTE: Reference python sc2scenarios --help for usage descriptions
from .functions import selectMap
from .mapRecord import standardizeMapName
from .          import constants

__version__ = "0.0.1"

