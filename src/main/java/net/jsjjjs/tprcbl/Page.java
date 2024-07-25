package net.jsjjjs.tprcbl;

public class Page {
    private String title = "A TPRCBL page";
    private Body body;

    public Page(Body body) {
        this.body = body;
    }
    public Page(String title, Body tprcbl) {
        this.title = title;
        this.body = tprcbl;
    }

    public String getTitle() {
        return title;
    }
    public void setTitle(String newTitle) {
        this.title = newTitle;
    }

    public Body getBody() {
        return body;
    }
    public void setBody(Body newBOdy) {
        this.body = newBOdy;
    }
}
