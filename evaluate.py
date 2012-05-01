import sublime
import sublime_plugin

class MathevalCommand(sublime_plugin.TextCommand):
    def run(self, edit, replace=True):
        
        selections = self.view.sel()
        
        for sel_points in selections:
            s = self.view.substr(sel_points)
            
            results = str(eval(s))
            self.view.replace(edit, sel_points, results)
