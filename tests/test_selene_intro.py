from selene.support.conditions import have
from selene.support.shared import browser

from selene_intro import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_complete_task():
    browser.open("http://todomvc.com/examples/emberjs/")

    # add tasks: "a", "b", "c"
    browser.element("#new-todo").type("a").press_enter()
    browser.element("#new-todo").type("b").press_enter()
    browser.element("#new-todo").type("c").press_enter()

    # tasks should be "a", "b", "c"
    browser.all(".todo-list > li.ember-view").should(have.exact_texts("a", "b", "c"))

    # toggle b
    b_element = browser.element(".todo-list > li.ember-view:nth-child(2) > * > .toggle")
    b_element.click()

    # completed tasks should be b
    browser.element(".todo-list > li.ember-view:nth-child(2)").should(have.text("b"))
    browser.element(".todo-list > li.ember-view:nth-child(2)").should(have.css_class("completed"))


    # active tasks should be a, c
    browser.element(".todo-list > li.ember-view:nth-child(1)").should(have.no.css_class("completed"))
    browser.element(".todo-list > li.ember-view:nth-child(1)").should(have.text("a"))
    browser.element(".todo-list > li.ember-view:nth-child(3)").should(have.no.css_class("completed"))
    browser.element(".todo-list > li.ember-view:nth-child(3)").should(have.text("c"))
