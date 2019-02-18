import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Qld_Gov_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'qld_gov_theme')

    def before_search(self, data_dict):
        """Create a UNION of the search results containing the desired tags."""
    	if 'seismic' and 'geochemistry' and 'dataset' in data_dict['fq']:
	    	fix = "tags:(seismic OR geochemistry OR dataset)"
	    	data_dict['fq'] = fix
    	return data_dict

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
