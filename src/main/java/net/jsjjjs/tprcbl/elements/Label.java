package net.jsjjjs.tprcbl.elements;

import org.jetbrains.annotations.NotNull;

public class Label implements Element {
    private @NotNull String innerText;

    private String color;

    public Label(@NotNull String innerText) {
        this.innerText = innerText;
    }

    public @NotNull String render() {
        return innerText;
    }

    public @NotNull String getInnerText() {
        return innerText;
    }

    public void setInnerText(@NotNull String newText) {
        innerText = newText;
    }

    public String getColor() {
        return this.color;
    }

    public void setColor(String color) {
        this.color = color;
    }
}
