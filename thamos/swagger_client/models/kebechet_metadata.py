# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.7.0-dev

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class KebechetMetadata(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'message_justification': 'int',
        'package_name': 'str',
        'package_version': 'str',
        'package_index': 'str'
    }

    attribute_map = {
        'message_justification': 'message_justification',
        'package_name': 'package_name',
        'package_version': 'package_version',
        'package_index': 'package_index'
    }

    def __init__(self, message_justification=None, package_name=None, package_version=None, package_index=None):  # noqa: E501
        """KebechetMetadata - a model defined in Swagger"""  # noqa: E501
        self._message_justification = None
        self._package_name = None
        self._package_version = None
        self._package_index = None
        self.discriminator = None
        if message_justification is not None:
            self.message_justification = message_justification
        if package_name is not None:
            self.package_name = package_name
        if package_version is not None:
            self.package_version = package_version
        if package_index is not None:
            self.package_index = package_index

    @property
    def message_justification(self):
        """Gets the message_justification of this KebechetMetadata.  # noqa: E501


        :return: The message_justification of this KebechetMetadata.  # noqa: E501
        :rtype: int
        """
        return self._message_justification

    @message_justification.setter
    def message_justification(self, message_justification):
        """Sets the message_justification of this KebechetMetadata.


        :param message_justification: The message_justification of this KebechetMetadata.  # noqa: E501
        :type: int
        """

        self._message_justification = message_justification

    @property
    def package_name(self):
        """Gets the package_name of this KebechetMetadata.  # noqa: E501


        :return: The package_name of this KebechetMetadata.  # noqa: E501
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this KebechetMetadata.


        :param package_name: The package_name of this KebechetMetadata.  # noqa: E501
        :type: str
        """

        self._package_name = package_name

    @property
    def package_version(self):
        """Gets the package_version of this KebechetMetadata.  # noqa: E501


        :return: The package_version of this KebechetMetadata.  # noqa: E501
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """Sets the package_version of this KebechetMetadata.


        :param package_version: The package_version of this KebechetMetadata.  # noqa: E501
        :type: str
        """

        self._package_version = package_version

    @property
    def package_index(self):
        """Gets the package_index of this KebechetMetadata.  # noqa: E501


        :return: The package_index of this KebechetMetadata.  # noqa: E501
        :rtype: str
        """
        return self._package_index

    @package_index.setter
    def package_index(self, package_index):
        """Sets the package_index of this KebechetMetadata.


        :param package_index: The package_index of this KebechetMetadata.  # noqa: E501
        :type: str
        """

        self._package_index = package_index

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(KebechetMetadata, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KebechetMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
