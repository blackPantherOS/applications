#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2009 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

import os
import glob
import shutil
import sys

from distutils.core import setup
from distutils.cmd import Command
from distutils.command.build import build
from distutils.command.install import install

import about

def update_messages():
    # Create empty directory
    os.system("rm -rf .tmp")
    os.makedirs(".tmp")
    # Collect UI files
    for filename in glob.glob1("module_gui", "*.ui"):
        os.system("pykdeuic4 -o .tmp/ui_%s.py module_gui/%s" % (filename.split(".")[0], filename))
    # Collect Python files
    for filename in glob.glob1("module_gui", "*.py"):
        shutil.copy("module_gui/%s" % filename, ".tmp")
    # Generate POT file
    os.system("xgettext --default-domain=%s --keyword=_ --keyword=i18n --keyword=ki18n -o po/%s.pot .tmp/*" % (about.catalog, about.catalog))
    # Update PO files
    for item in os.listdir("po"):
        if item.endswith(".po"):
            os.system("msgmerge -q -o .tmp/temp.po po/%s po/%s.pot" % (item, about.catalog))
            os.system("cp .tmp/temp.po po/%s" % item)
    # Remove temporary directory
    os.system("rm -rf .tmp")

def makeDirs(dir):
    try:
        os.makedirs(dir)
    except OSError:
        pass

class Build(build):
    def run(self):
        # Clear all
        os.system("rm -rf build")
        # Copy codes
        print "Copying PYs..."
        os.system("cp -R src build/")
        # Copy compiled UIs and RCs
        print "Generating UIs..."
        for filename in glob.glob1("module_gui", "*.ui"):
            os.system("pykdeuic4 -o build/gui/%s.py module_gui/%s" % (filename.split(".")[0], filename))
        print "Generating RCs..."
        for filename in glob.glob1("module_gui", "*.qrc"):
            os.system("pyrcc4 module_gui/%s -o build/%s_rc.py" % (filename, filename.split(".")[0]))

class Install(install):
    def run(self):
        os.system("./setup.py build")
        if self.root:
            kde_dir = "%s/usr" % self.root
        else:
            kde_dir = "/usr/share/kde4"
        bin_dir = os.path.join(kde_dir, "bin")
        locale_dir = os.path.join(kde_dir, "share/locale")
        autostart_dir = os.path.join(kde_dir, "share/autostart")
        project_dir = os.path.join(kde_dir, "share/apps", about.appName)
        # Make directories
        print "Making directories..."
        sys.exit()
        makeDirs(bin_dir)
        #makeDirs(locale_dir)
        makeDirs(autostart_dir)
        makeDirs(project_dir)
        # Install desktop files
        print "Installing desktop files..."
        for filename in glob.glob1("data", "*.desktop"):
            shutil.copy("data/%s" % filename, autostart_dir)
        # Install codes
        print "Installing codes..."
        os.system("cp -R build/* %s/" % project_dir)
        # Install locales
        print "Installing locales..."
        for filename in glob.glob1("po", "*.po"):
            lang = filename.rsplit(".", 1)[0]
            os.system("msgfmt po/%s.po -o po/%s.mo" % (lang, lang))
            try:
                os.makedirs(os.path.join(locale_dir, "%s/LC_MESSAGES" % lang))
            except OSError:
                pass
            shutil.copy("po/%s.mo" % lang, os.path.join(locale_dir, "%s/LC_MESSAGES" % lang, "%s.mo" % about.catalog))
        # Rename
        print "Renaming application.py..."
        #shutil.move(os.path.join(project_dir, "application.py"), os.path.join(project_dir, "%s.py" % about.appName))
        # Modes
        print "Changing file modes..."
        os.chmod(os.path.join(project_dir, "%s.py" % about.appName), 0755)
        # Symlink
        try:
            if self.root:
                os.symlink(os.path.join(project_dir.replace(self.root, ""), "%s.py" % about.appName), os.path.join(bin_dir, about.appName))
            else:
                os.symlink(os.path.join(project_dir, "%s.py" % about.appName), os.path.join(bin_dir, about.appName))
        except OSError:
            pass


if "update_messages" in sys.argv:
    update_messages()
    sys.exit(0)

setup(
      name              = about.appName,
      version           = about.version,
      description       = unicode(about.description),
      license           = unicode(about.license),
      author            = "",
      author_email      = about.bugEmail,
      url               = about.homePage,
      packages          = [''],
      package_dir       = {'': ''},
      data_files        = [],
      cmdclass          = {
                            'build': Build,
                            'install': Install,
                          }
)
