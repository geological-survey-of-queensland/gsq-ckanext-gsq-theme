import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Qld_Gov_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'qld_gov_theme')

    # The permit route for header pill navigation button
    # Reference: https://stackoverflow.com/questions/17777191/how-to-add-a-menu-item-to-ckans-naivigation-menu
    def before_map(self, m):
    	m.connect(
    		'permit_search',
    		'',
    		controller = 'ckanext.qld_gov_theme.controller:PermitController',
    		action = 'permit'
    	)
    	return m