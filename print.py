import sublime, sublime_plugin

# class CreateNewWindowCommand(sublime_plugin.WindowCommand):
#     def run(self):
#         s = self.window.active_view().substr(sublime.Region(0, self.window.active_view().size()))
#         newFile = self.window.new_file()
#         newFile.run_command("copy_text",{"textBuffer" : s})

# class CopyTextCommand(sublime_plugin.TextCommand):
#     def printAChar(self,char,edit):
#         self.view.insert(edit, self.view.size(), char)

#     def run(self, edit, textBuffer):
#         s = list(textBuffer)
#         for i in s:
#             self.printAChar(i, edit)




class PrintCodeCommand(sublime_plugin.WindowCommand):
    def run(self):
        # self.window.run_command("create_new_window")
        def makeTimeout(time, text): sublime.set_timeout(lambda : print(text),time)
        for x in range(1,10):
            makeTimeout(x*1000,x)