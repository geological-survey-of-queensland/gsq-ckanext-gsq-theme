import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckantoolkit import config
from ckan.lib import helpers
import inspect

# Changed to remove dependency on ckanext-dcat
def get_dataset_rdf_url(default=False):
    url = toolkit.request.url
    url = url.split('?')[0]
    dataset_name = url.split('/')[-1]
    dataset_type = toolkit.get_action('package_show')(None, {'id': dataset_name})['type']

    uri = config.get('ckanext.dcat.base_uri')
    if not uri:
        uri = config.get('ckan.site_url')

    if default:
        return uri + '/' + 'dataset' + '/' + dataset_name # + '.ttl?profiles=gsq_dataset'
    else:
        return uri + '/' + 'dataset' + '/' + dataset_name # + '.ttl?profiles=gsq_' + dataset_type + ',gsq_dataset'

# Changed to remove dependency on ckanext-dcat
def get_dataset_rdf_name(default=False, id=None):
    if id:
        dataset_type = toolkit.get_action('package_show')(None, {'id': id})['type']
    else:
        url = toolkit.request.url
        url = url.split('?')[0]
        dataset_name = url.split('/')[-1]
        dataset_type = toolkit.get_action('package_show')(None, {'id': dataset_name})['type']
    
    if default:
        display_name = 'dcat_' + 'dataset' + '_profile' + '.ttl'
    else:
        display_name = 'gsq_' + dataset_type + '_profile' + '.ttl'
    # Return blank string so no TTL link appears in the dataset page
    return '' # display_name


def get_dataset_type():
    url = toolkit.request.url
    url = url.split('?')[0]
    dataset_name = url.split('/')[-1]
    return toolkit.get_action('package_show')(None, {'id': dataset_name})['type']



class Qld_Gov_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'qld_gov_theme')

    def get_helpers(self):
        return {
            'get_rdf_url': get_dataset_rdf_url,
            'get_rdf_name': get_dataset_rdf_name,
            'get_type': get_dataset_type,
        }

# def before_search(self, data_dict):
#         """Create a UNION of the search results containing the desired tags."""
#         args = data_dict['fq'].split(' ')
#         tags = []
#         for arg in args:
#             if 'tags:' in arg and 'seismic' in arg:
#                 tags.append('seismic')
#             if 'tags:' in arg and 'geochemistry' in arg:
#                 tags.append('geochemistry')
#             if 'tags:' in arg and 'dataset' in arg:
#                 tags.append('dataset')
        
#         if tags:
#             fix = 'tags:('
#             for i, tag in enumerate(tags):
#                 if i > 0:
#                     fix += ' OR '
#                 fix += tag
            
#             fix += ')'
#             data_dict['fq'] = fix

#     	return data_dict

    # The permit route for header pill navigation button
    # Reference: https://stackoverflow.com/questions/17777191/how-to-add-a-menu-item-to-ckans-naivigation-menu
    # def before_map(self, m):
    # 	m.connect(
    # 		'dataset',
    # 		'/dataset',
    # 		controller='ckanext.qld_gov_theme.controller:NewDatasetController',
    # 		action='dataset'
    # 	)
    # 	# return toolkit.url_for('http://www.google.com')
    # 	return m
