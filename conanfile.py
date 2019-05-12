import os

from conans import ConanFile, tools


class StbConan(ConanFile):
    name = "stb"
    version = "20190512"
    license = "Public domain"
    url = "https://github.com/conan-community/conan-stb"
    description = "stb single-file public domain libraries for C/C++ https://twitter.com/nothings"
    no_copy_source = True

    def source(self):
        a_hash = {"20190512": "1034f5e"}[str(self.version)]
        self.run("git clone https://github.com/nothings/stb.git")
        with tools.chdir("stb"):
            self.run("git reset --hard %s" % a_hash)

        if os.getenv("CONAN_RUN_TESTS", False):
            if not tools.os_info.is_windows:
                tools.replace_in_file(os.path.join('stb', 'tests', 'Makefile'),
                                      '-DSTB_DIVIDE_TEST',
                                      '-DSTB_DIVIDE_TEST -DSTB_TEXTEDIT_KEYTYPE=unsigned')
                with tools.chdir("stb/tests"):
                    self.run("make all")

    def package(self):
        self.copy("*.h", src="stb", dst="include")
        self.copy("*why_public_domain.md", src="stb", dst="licenses", keep_path=False)

    def package_info(self):
        self.cpp_info.defines.append('STB_TEXTEDIT_KEYTYPE=unsigned')
