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
    '--include {path}/common/static/styl',  # Expose common styl lib dir
    '--use kouto-swiss',
]).format(path=BASE_DIR)

# Packaging specs for CSS
PIPELINE_CSS = {
    'common': {
        'source_filenames': [
            'styl/common/*.styl',
        ],
        'output_filename': 'css/common.css',
    },
    'guideline': {
        'source_filenames': ['guideline/styl/*.styl'],
        'output_filename': 'css/guideline.css',
    },
    'accounts': {
        'source_filenames': ['styl/accounts-*.styl'],
        'output_filename': 'css/accounts.css',
    }
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
}
