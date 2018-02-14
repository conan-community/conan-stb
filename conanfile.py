import os

from conans import ConanFile, tools


class StbConan(ConanFile):
    name = "stb"
    version = "20180214"
    license = "Public domain"
    url = "https://github.com/conan-community/conan-stb"
    description = "stb single-file public domain libraries for C/C++ https://twitter.com/nothings"
    no_copy_source = True

    def source(self):
        a_hash = {"20180214": "e6afb9c"}[str(self.version)]
        self.run("git clone https://github.com/nothings/stb.git")
        with tools.chdir("stb"):
            self.run("git reset --hard %s" % a_hash)

        if os.getenv("CONAN_RUN_TESTS", False):
            if not tools.os_info.is_windows:
                with tools.chdir("stb/tests"):
                    self.run("make all")

    def package(self):
        self.copy("*.h", src="stb", dst="include")
