import sublime, sublime_plugin

class PrintCodeCommand(sublime_plugin.WindowCommand):
    def run(self):
        syntax = self.window.active_view().settings().get('syntax')
        allString = self.window.active_view().substr(sublime.Region(0, self.window.active_view().size()))
        newFile = self.window.new_file()
        newFile.set_syntax_file(syntax)
        t = 0 # timer
        a = "add" # add, remove, clear
        for c in  allString:
            if c == 'é':
                a = "remove"
            elif c == 'è':
                a = "clear"
            else : 
                a = "add"
            sublime.set_timeout(lambda char = c, action = a : newFile.run_command("process_char_action",{ "action" : action , "char" : char}) , t*100)
            t += 1

class ProcessCharActionCommand(sublime_plugin.TextCommand):
    def run(self, edit, action, char):
        if action == "add":
            self.view.insert(edit, self.view.size(), char)
        elif action == "remove":
            region = sublime.Region(self.view.size()-1, self.view.size())
            self.view.erase(edit, region)
        elif action == "clear" :
            region = sublime.Region(0, self.view.size())
            self.view.erase(edit, region)