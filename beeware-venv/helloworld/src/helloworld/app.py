"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class HelloWorld(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        # 创建一个主框
        main_box = toga.Box(style=Pack(direction=COLUMN))  # 这里的COLUMN决定了其内部件的排列顺序——上下。
        """
        style应用样式：
        Toga 的内置布局系统称为“Pack”。
        它的行为很像 CSS。
        你在一个层次定义对象-在HTML中，对象<div>，<span>以及其他DOM元素; 
        在 Toga 中，它们是小部件和盒子。
        然后，您可以为各个元素分配样式。
        在这种情况下，我们表示这是一个COLUMN盒子——也就是说，
        它是一个会消耗所有可用宽度的盒子，并且会随着内容的添加而扩展其高度，但它会尽量缩短。
        """

        # 创建两个部件：1个标签
        name_label = toga.Label('Your name: ', style=Pack(padding=(0, 5)))  # padding是用来设置部件的上下、左右间距（上下, 左右）
        # 1个输入框，输入框中的值，后续需要使用，因此定义为类变量
        self.name_input = toga.TextInput(style=Pack(flex=1))  # flex是指flexible灵活的，即输入框将占用所有可用空间
        """
        两个小部件都有与之关联的样式；
        Label 将在其左侧和右侧有 5px 的填充，顶部和底部没有填充。
        TextInput 被标记为灵活的——也就是说，它将吸收其布局轴上的所有可用空间。
        TextInput 被分配为类的实例变量。这使我们可以轻松访问小部件实例 - 我们稍后将使用它。
        """
        # 创建一个子框 name_box
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))  # ROW——左右排列，padding的值是单一数据，说明上下左右都是5px
        """
        name_box是一个和主盒子一样的盒子；
        然而，这一次，它是一个 ROW盒子。这意味着内容将被水平添加，
        并且它会尝试使其宽度尽可能窄。盒子还有一些内边距——四面都是 5px。
        """
        # 使用add方法，将部件放入框内
        name_box.add(name_label)
        name_box.add(self.name_input)

        # 创建一个按钮
        button = toga.Button(
            'Say Hello!',
            on_press=self.sayhello,
            style=Pack(padding=5)
        )
        """
        该按钮的四边也有 5px 的内边距。
        我们还定义了一个处理程序——一个在按钮被按下时调用的方法。
        """
        # 在主框中添加子框和按钮
        main_box.add(name_box)
        main_box.add(button)

        # 创建一个根窗口
        self.main_window = toga.MainWindow(title=self.formal_name)
        # 将主框放入根窗口内
        self.main_window.content = main_box
        # 显示窗口
        self.main_window.show()

    def sayhello(self, widget):
        # print('Hello,', self.name_input.value)
        """
        加一个对话框来打招呼，而不是写到控制台
        判断输入框内是否有值
        :param widget:
        :return:
        """
        if self.name_input.value:
            name = self.name_input.value
        else:
            name = 'stranger'
        self.main_window.info_dialog(
            'Hi, there!',
            f"Hello, {self.name_input.value}"
        )


def main():
    return HelloWorld()
