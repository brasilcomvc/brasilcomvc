import os
import sys


# Main project directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
STATIC_BASE_DIR = os.path.join(BASE_DIR, '../webroot')

# Static file dirs
STATIC_ROOT = os.path.join(STATIC_BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(STATIC_BASE_DIR, 'media')

# Static file URLs
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# django-pipeline settings

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
if 'test' in sys.argv:
    STATICFILES_STORAGE = 'pipeline.storage.NonPackagingPipelineStorage'

STATICFILES_FINDERS = (
    'pipeline.finders.FileSystemFinder',
    'pipeline.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../bower_components'),
)
PIPELINE_COMPILERS = (
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
    'pipeline.compilers.stylus.StylusCompiler',
)

# Stylus configuration
PIPELINE_STYLUS_ARGUMENTS = ' '.join([
    '--include {path}/common/static/styl/_global',  # Expose global .styl libs
    '--use kouto-swiss',
]).format(path=BASE_DIR)

# JavaScript configuration
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'

# Packaging specs for CSS
PIPELINE_CSS = {
    'common': {
        'source_filenames': ['styl/common-manifest.styl'],
        'output_filename': 'css/common.css',
    },
    'guideline': {
        'source_filenames': ['guideline/styl/*.styl'],
        'output_filename': 'css/guideline.css',
    },
    'accounts': {
        'source_filenames': ['styl/accounts-manifest.styl'],
        'output_filename': 'css/accounts.css',
    },
    'projects': {
        'source_filenames': ['styl/projects-manifest.styl'],
        'output_filename': 'css/projects.css',
    },
}

# Packaging specs for JavaScript
PIPELINE_JS = {
    '3rdparty': {
        'source_filenames': (
            'jquery/dist/jquery.js',
        ),
        'output_filename': '3rdparty.js',
    },
    'common': {
        'source_filenames': ['coffee/common-*.coffee'],
        'output_filename': 'js/common.js',
    },
    'accounts': {
        'source_filenames': ['coffee/accounts-*.coffee'],
        'output_filename': 'js/accounts.js',
    },
    'projects': {
        'source_filenames': ['coffee/projects-*.coffee'],
        'output_filename': 'js/projects.js',
    },
}

# Binaries (this settings assumes you've installed all node modules locally)
_node_modules = os.path.join(BASE_DIR, '../node_modules/.bin')
PIPELINE_COFFEE_SCRIPT_BINARY = os.path.join(_node_modules, 'coffee')
PIPELINE_STYLUS_BINARY = os.path.join(_node_modules, 'stylus')
PIPELINE_YUGLIFY_BINARY = os.path.join(_node_modules, 'yuglify')

# Statics on S3
if os.environ.get('STATIC_BACKEND', 'local') == 's3':
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_CUSTOM_DOMAIN = os.environ.get(
        'AWS_S3_CUSTOM_DOMAIN',
        '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME))
    AWS_S3_URL_PROTOCOL = 'https:'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATIC_URL = '%s//%s/' % (AWS_S3_URL_PROTOCOL, AWS_S3_CUSTOM_DOMAIN)

    STATICFILES_STORAGE = 'brasilcomvc.s3static.S3PipelineStorage'
