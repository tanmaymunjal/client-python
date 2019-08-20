import requests
from .utils import filter_list


class Templates:
    """
    Instances are built from a template. Templates may be either a base OS install such as Ubuntu 14.04 LTS,
    a control-panel based hosting setup or a fully setup application ready to configure for your use.
    """

    def __init__(self, headers):
        self.headers = headers
        self.url = 'https://api.civo.com/v2/templates'

    def create(self, code: str, id: str = None, name: str = None, volume_id: str = None, image_id: str = None,
               short_description: str = None, description: str = None, default_username: str = None,
               cloud_config: str = None) -> dict:
        """
        Function to create a new template
        :param id: This is a short identifier for the template, it should be lowercase letters, dashs, underscores,
                   full stop/periods and numbers only (optional: defaults to a new UUID).
        :param code: This is a unqiue, alphanumerical, short, human readable code for the template (required).
        :param name: This is a short human readable name for the template (optional).
        :param volume_id: This is the ID of a bootable volume, either owned by you or global
                          (optional; but must be specified if no image_id is specified).
        :param image_id: This is the Openstack Glance Image ID or the ID of another template,
                         either owned by you or global (optional; but must be specified if no volume_id is specified).
        :param short_description: A one line description of the template (optional)
        :param description: A multi-line description of the template, in Markdown format (optional).
        :param default_username: he default username to suggest that the user creates (optional: defaults to civo).
        :param cloud_config: Commonly referred to as 'user-data', this is a customisation script that is run after
                             the instance is first booted. We recommend using cloud-config as it's a great
                             distribution-agnostic way of configuring cloud servers.
                             If you put $INITIAL_USER in your script, this will automatically be replaced
                             by the initial user chosen when creating the instance, $INITIAL_PASSWORD will be
                             replaced with the random password generated by the system, $HOSTNAME is the fully
                             qualified domain name of the instance and $SSH_KEY
                             will be the content of the SSH public key.
                             (this is technically optional, but you won't really be able to use instances without it
                             see our learn guide on templates for more information)
        :return: object json
        """
        payload = {'code': code}

        if id:
            payload['id'] = id

        if name:
            payload['name'] = name

        if volume_id:
            payload['volume_id'] = volume_id

        if image_id:
            payload['image_id'] = image_id

        if short_description:
            payload['short_description'] = short_description

        if description:
            payload['description'] = description

        if default_username:
            payload['default_username'] = default_username

        if cloud_config:
            files = {'cloud_config': open(cloud_config, 'rb')}
            r = requests.get(self.url, headers=self.headers, files=files, params=payload)
        else:
            r = requests.get(self.url, headers=self.headers, params=payload)

        return r.json()

    def lists(self, filter: str = None) -> dict:
        """
        Function to listing available templates
        :param filter: Filter json object the format is 'id:6224cd2b-d416-4e92-bdbb-db60521c8eb9',
                       you can filter by any object that is inside the json
        :return: object json
        """
        r = requests.get(self.url, headers=self.headers)

        if filter:
            data = r.json()
            return filter_list(data=data, filter=filter)

        return r.json()

    def update(self, template_id: str, code: str, id: str = None, name: str = None, volume_id: str = None, image_id: str = None,
               short_description: str = None, description: str = None, default_username: str = None,
               cloud_config: str = None):
        """
        Function to create a new template
        :param template_id: id of template to update
        :param id: This is a short identifier for the template, it should be lowercase letters, dashs, underscores,
                   full stop/periods and numbers only (optional: defaults to a new UUID).
        :param code: This is a unqiue, alphanumerical, short, human readable code for the template (required).
        :param name: This is a short human readable name for the template (optional).
        :param volume_id: This is the ID of a bootable volume, either owned by you or global
                          (optional; but must be specified if no image_id is specified).
        :param image_id: This is the Openstack Glance Image ID or the ID of another template,
                         either owned by you or global (optional; but must be specified if no volume_id is specified).
        :param short_description: A one line description of the template (optional)
        :param description: A multi-line description of the template, in Markdown format (optional).
        :param default_username: he default username to suggest that the user creates (optional: defaults to civo).
        :param cloud_config: Commonly referred to as 'user-data', this is a customisation script that is run after
                             the instance is first booted. We recommend using cloud-config as it's a great
                             distribution-agnostic way of configuring cloud servers.
                             If you put $INITIAL_USER in your script, this will automatically be replaced
                             by the initial user chosen when creating the instance, $INITIAL_PASSWORD will be
                             replaced with the random password generated by the system, $HOSTNAME is the fully
                             qualified domain name of the instance and $SSH_KEY
                             will be the content of the SSH public key.
                             (this is technically optional, but you won't really be able to use instances without it
                             see our learn guide on templates for more information)
        :return: object json
        """
        payload = {'code': code}

        if id:
            payload['id'] = id

        if name:
            payload['name'] = name

        if volume_id:
            payload['volume_id'] = volume_id

        if image_id:
            payload['image_id'] = image_id

        if short_description:
            payload['short_description'] = short_description

        if description:
            payload['description'] = description

        if default_username:
            payload['default_username'] = default_username

        if cloud_config:
            files = {'cloud_config': open(cloud_config, 'rb')}
            r = requests.put(self.url + '/{}'.format(template_id), headers=self.headers, files=files, params=payload)
        else:
            r = requests.put(self.url + '/{}'.format(template_id), headers=self.headers, params=payload)

        return r.json()

    def delete(self, template_id: str) -> dict:
        """
        Function to deleting a template
        :param template_id: id of template to delete
        :return: object json
        """
        r = requests.delete(self.url + '/{}'.format(template_id), headers=self.headers)

        return r.json()