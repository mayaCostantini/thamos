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

class AnalysisResultResponseMetadataDistribution(object):
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
        'codename': 'str',
        'id': 'str',
        'like': 'str',
        'version': 'str',
        'version_parts': 'AnalysisResultResponseMetadataDistributionVersionParts'
    }

    attribute_map = {
        'codename': 'codename',
        'id': 'id',
        'like': 'like',
        'version': 'version',
        'version_parts': 'version_parts'
    }

    def __init__(self, codename=None, id=None, like=None, version=None, version_parts=None):  # noqa: E501
        """AnalysisResultResponseMetadataDistribution - a model defined in Swagger"""  # noqa: E501
        self._codename = None
        self._id = None
        self._like = None
        self._version = None
        self._version_parts = None
        self.discriminator = None
        self.codename = codename
        self.id = id
        self.like = like
        self.version = version
        self.version_parts = version_parts

    @property
    def codename(self):
        """Gets the codename of this AnalysisResultResponseMetadataDistribution.  # noqa: E501

        Codename of environment in which the analysis was performed   # noqa: E501

        :return: The codename of this AnalysisResultResponseMetadataDistribution.  # noqa: E501
        :rtype: str
        """
        return self._codename

    @codename.setter
    def codename(self, codename):
        """Sets the codename of this AnalysisResultResponseMetadataDistribution.

        Codename of environment in which the analysis was performed   # noqa: E501

        :param codename: The codename of this AnalysisResultResponseMetadataDistribution.  # noqa: E501
        :type: str
        """
        if codename is None:
            raise ValueError("Invalid value for `codename`, must not be `None`")  # noqa: E501

        self._codename = codename

    @property
    def id(self):
        """Gets the id of this AnalysisResultResponseMetadataDistribution.  # noqa: E501

        Identifier of environment in which the analysis was performed   # noqa: E501

        :return: The id of this AnalysisResultResponseMetadataDistribution.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnalysisResultResponseMetadataDistribution.

        Identifier of environment in which the analysis was performed   # noqa: E501

        :param id: The id of this AnalysisResultResponseMetadataDistribution.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def like(self):
        """Gets the like of this AnalysisResultResponseMetadataDistribution.  # noqa: E501

        Similar environments in comparison to environment in which the analysis was performed   # noqa: E501

        :return: The like of this AnalysisResultResponseMetadataDistribution.  # noqa: E501
        :rtype: str
        """
        return self._like

    @like.setter
    def like(self, like):
        """Sets the like of this AnalysisResultResponseMetadataDistribution.

        Similar environments in comparison to environment in which the analysis was performed   # noqa: E501

        :param like: The like of this AnalysisResultResponseMetadataDistribution.  # noqa: E501
        :type: str
        """
        if like is None:
            raise ValueError("Invalid value for `like`, must not be `None`")  # noqa: E501

        self._like = like

    @property
    def version(self):
        """Gets the version of this AnalysisResultResponseMetadataDistribution.  # noqa: E501

        A string representation of environment version  # noqa: E501

        :return: The version of this AnalysisResultResponseMetadataDistribution.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AnalysisResultResponseMetadataDistribution.

        A string representation of environment version  # noqa: E501

        :param version: The version of this AnalysisResultResponseMetadataDistribution.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def version_parts(self):
        """Gets the version_parts of this AnalysisResultResponseMetadataDistribution.  # noqa: E501


        :return: The version_parts of this AnalysisResultResponseMetadataDistribution.  # noqa: E501
        :rtype: AnalysisResultResponseMetadataDistributionVersionParts
        """
        return self._version_parts

    @version_parts.setter
    def version_parts(self, version_parts):
        """Sets the version_parts of this AnalysisResultResponseMetadataDistribution.


        :param version_parts: The version_parts of this AnalysisResultResponseMetadataDistribution.  # noqa: E501
        :type: AnalysisResultResponseMetadataDistributionVersionParts
        """
        if version_parts is None:
            raise ValueError("Invalid value for `version_parts`, must not be `None`")  # noqa: E501

        self._version_parts = version_parts

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
        if issubclass(AnalysisResultResponseMetadataDistribution, dict):
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
        if not isinstance(other, AnalysisResultResponseMetadataDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
