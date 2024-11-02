#define UNICODE
#include <regex>
#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <locale>
#include <codecvt>
#include <vector>
#include <Windows.h>

// https://stackoverflow.com/q/55582966/6748004
std::string get_file_contents(const char *filename)
{
  std::ifstream in(filename, std::ios::in | std::ios::binary);
  if (in)
  {
    return(std::string((std::istreambuf_iterator<char>(in)), std::istreambuf_iterator<char>()));
  }
  throw(errno);
}

int main() {
    SetConsoleOutputCP(CP_UTF8);
    // https://stackoverflow.com/a/8187099/6748004
    LPWSTR *szArglist;
    int argc;
    szArglist = CommandLineToArgvW(GetCommandLineW(),&argc);
    if(NULL==szArglist) {
        return -1;
    }
    if (argc != 2) {
        return -1;
    }
    std::wstring_convert<std::codecvt_utf8_utf16<wchar_t>,wchar_t> convert; // codecvt_utf8 or codecvt<char16_t,char,mbstate_t> should work (will work once the char16_t specialization of codecvt works)
    std::vector<std::string> args;
    for(int i=0;i<argc;++i) {
        args.push_back(convert.to_bytes(szArglist[i]));
    }
    auto text = args[1];
    auto regex = get_file_contents("out/regex.txt");
    std::regex const e{ regex }; 
    std::string s(text);
    std::smatch m;
    if (std::regex_match(s, m, e)) {
        std::cout << "1";
    }
    else {
        std::cout << "0";
    }
}
