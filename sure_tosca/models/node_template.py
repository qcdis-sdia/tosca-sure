# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from sure_tosca.models.base_model_ import Model
from sure_tosca import util


class NodeTemplateModel(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, derived_from=None, properties=None, requirements=None, interfaces=None, capabilities=None, type=None, description=None, directives=None, attributes=None, artifacts=None):  # noqa: E501
        """NodeTemplate - a model defined in Swagger

        :param derived_from: The derived_from of this NodeTemplate.  # noqa: E501
        :type derived_from: str
        :param properties: The properties of this NodeTemplate.  # noqa: E501
        :type properties: Dict[str, object]
        :param requirements: The requirements of this NodeTemplate.  # noqa: E501
        :type requirements: List[Dict[str, object]]
        :param interfaces: The interfaces of this NodeTemplate.  # noqa: E501
        :type interfaces: Dict[str, object]
        :param capabilities: The capabilities of this NodeTemplate.  # noqa: E501
        :type capabilities: Dict[str, object]
        :param type: The type of this NodeTemplate.  # noqa: E501
        :type type: str
        :param description: The description of this NodeTemplate.  # noqa: E501
        :type description: str
        :param directives: The directives of this NodeTemplate.  # noqa: E501
        :type directives: List[str]
        :param attributes: The attributes of this NodeTemplate.  # noqa: E501
        :type attributes: Dict[str, object]
        :param artifacts: The artifacts of this NodeTemplate.  # noqa: E501
        :type artifacts: Dict[str, object]
        """
        self.swagger_types = {
            'derived_from': str,
            'properties': Dict[str, object],
            'requirements': List[Dict[str, object]],
            'interfaces': Dict[str, object],
            'capabilities': Dict[str, object],
            'type': str,
            'description': str,
            'directives': List[str],
            'attributes': Dict[str, object],
            'artifacts': Dict[str, object]
        }

        self.attribute_map = {
            'derived_from': 'derived_from',
            'properties': 'properties',
            'requirements': 'requirements',
            'interfaces': 'interfaces',
            'capabilities': 'capabilities',
            'type': 'type',
            'description': 'description',
            'directives': 'directives',
            'attributes': 'attributes',
            'artifacts': 'artifacts'
        }

        self._derived_from = derived_from
        self._properties = properties
        self._requirements = requirements
        self._interfaces = interfaces
        self._capabilities = capabilities
        self._type = type
        self._description = description
        self._directives = directives
        self._attributes = attributes
        self._artifacts = artifacts

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NodeTemplate of this NodeTemplate.  # noqa: E501
        :rtype: NodeTemplateModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def derived_from(self):
        """Gets the derived_from of this NodeTemplate.


        :return: The derived_from of this NodeTemplate.
        :rtype: str
        """
        return self._derived_from

    @derived_from.setter
    def derived_from(self, derived_from):
        """Sets the derived_from of this NodeTemplate.


        :param derived_from: The derived_from of this NodeTemplate.
        :type derived_from: str
        """

        self._derived_from = derived_from

    @property
    def properties(self):
        """Gets the properties of this NodeTemplate.


        :return: The properties of this NodeTemplate.
        :rtype: Dict[str, object]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this NodeTemplate.


        :param properties: The properties of this NodeTemplate.
        :type properties: Dict[str, object]
        """

        self._properties = properties

    @property
    def requirements(self):
        """Gets the requirements of this NodeTemplate.


        :return: The requirements of this NodeTemplate.
        :rtype: List[Dict[str, object]]
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """Sets the requirements of this NodeTemplate.


        :param requirements: The requirements of this NodeTemplate.
        :type requirements: List[Dict[str, object]]
        """

        self._requirements = requirements

    @property
    def interfaces(self):
        """Gets the interfaces of this NodeTemplate.


        :return: The interfaces of this NodeTemplate.
        :rtype: Dict[str, object]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """Sets the interfaces of this NodeTemplate.


        :param interfaces: The interfaces of this NodeTemplate.
        :type interfaces: Dict[str, object]
        """

        self._interfaces = interfaces

    @property
    def capabilities(self):
        """Gets the capabilities of this NodeTemplate.


        :return: The capabilities of this NodeTemplate.
        :rtype: Dict[str, object]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this NodeTemplate.


        :param capabilities: The capabilities of this NodeTemplate.
        :type capabilities: Dict[str, object]
        """

        self._capabilities = capabilities

    @property
    def type(self):
        """Gets the type of this NodeTemplate.


        :return: The type of this NodeTemplate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodeTemplate.


        :param type: The type of this NodeTemplate.
        :type type: str
        """

        self._type = type

    @property
    def description(self):
        """Gets the description of this NodeTemplate.


        :return: The description of this NodeTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NodeTemplate.


        :param description: The description of this NodeTemplate.
        :type description: str
        """

        self._description = description

    @property
    def directives(self):
        """Gets the directives of this NodeTemplate.


        :return: The directives of this NodeTemplate.
        :rtype: List[str]
        """
        return self._directives

    @directives.setter
    def directives(self, directives):
        """Sets the directives of this NodeTemplate.


        :param directives: The directives of this NodeTemplate.
        :type directives: List[str]
        """

        self._directives = directives

    @property
    def attributes(self):
        """Gets the attributes of this NodeTemplate.


        :return: The attributes of this NodeTemplate.
        :rtype: Dict[str, object]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this NodeTemplate.


        :param attributes: The attributes of this NodeTemplate.
        :type attributes: Dict[str, object]
        """

        self._attributes = attributes

    @property
    def artifacts(self):
        """Gets the artifacts of this NodeTemplate.


        :return: The artifacts of this NodeTemplate.
        :rtype: Dict[str, object]
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        """Sets the artifacts of this NodeTemplate.


        :param artifacts: The artifacts of this NodeTemplate.
        :type artifacts: Dict[str, object]
        """

        self._artifacts = artifacts