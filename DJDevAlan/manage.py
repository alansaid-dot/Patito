#!/usr/bin/env python
import os
import sys

def main():
    # PARA RENDER - usa producción
    # PARA LOCAL - comenta esta línea
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'empleado.settings.prod')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()