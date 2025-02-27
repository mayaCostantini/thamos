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

class BuildAnalysisResponseErrorOutputImageAnalysis(object):
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
        'error': 'str',
        'parameters': 'object'
    }

    attribute_map = {
        'error': 'error',
        'parameters': 'parameters'
    }

    def __init__(self, error=None, parameters=None):  # noqa: E501
        """BuildAnalysisResponseErrorOutputImageAnalysis - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._parameters = None
        self.discriminator = None
        if error is not None:
            self.error = error
        if parameters is not None:
            self.parameters = parameters

    @property
    def error(self):
        """Gets the error of this BuildAnalysisResponseErrorOutputImageAnalysis.  # noqa: E501

        Error information for user  # noqa: E501

        :return: The error of this BuildAnalysisResponseErrorOutputImageAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this BuildAnalysisResponseErrorOutputImageAnalysis.

        Error information for user  # noqa: E501

        :param error: The error of this BuildAnalysisResponseErrorOutputImageAnalysis.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def parameters(self):
        """Gets the parameters of this BuildAnalysisResponseErrorOutputImageAnalysis.  # noqa: E501

        Parameters echoed back to user for debugging  # noqa: E501

        :return: The parameters of this BuildAnalysisResponseErrorOutputImageAnalysis.  # noqa: E501
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this BuildAnalysisResponseErrorOutputImageAnalysis.

        Parameters echoed back to user for debugging  # noqa: E501

        :param parameters: The parameters of this BuildAnalysisResponseErrorOutputImageAnalysis.  # noqa: E501
        :type: object
        """

        self._parameters = parameters

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
        if issubclass(BuildAnalysisResponseErrorOutputImageAnalysis, dict):
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
        if not isinstance(other, BuildAnalysisResponseErrorOutputImageAnalysis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
