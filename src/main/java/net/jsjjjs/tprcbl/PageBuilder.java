package net.jsjjjs.tprcbl;

import net.jsjjjs.tprcbl.elements.Element;
import net.jsjjjs.tprcbl.registries.ElementRegistry;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;

public class PageBuilder {
    private JSONObject code;

    public PageBuilder(JSONObject code){
        this.code = code;
    }

    public Page build() throws NoSuchMethodException, InvocationTargetException, InstantiationException, IllegalAccessException {
        JSONArray body = (JSONArray) code.get("body");
        Element[] elements = new Element[body.size()];
        for (int i = 0; i < body.size(); i++) {
            JSONArray element = (JSONArray) body.get(i);
            Class<? extends Element> elementClass = ElementRegistry.valueOf(((String) element.get(0)).toUpperCase()).getElementClass();
            Object[] args = new Object[element.size() - 1];
            Class<?>[] argTypes = new Class[args.length];
            for (int j = 1; j < element.size(); j++) {
                args[j - 1] = element.get(j);
                argTypes[j - 1] = args[j - 1].getClass();
            }
            Constructor<?> constructor = elementClass.getConstructor(argTypes);
            elements[i] = (Element) constructor.newInstance(args);
        }
        if (code.get("title") != null) {
            return new Page((String) code.get("title"), new Body(elements));
        }
        return new Page(new Body(elements));
    }

    public PageBuilder ChangeCode(JSONObject newCode) {
        return new PageBuilder(newCode);
    }
    public PageBuilder changeTitle(String newTitle) {
        this.code.put("title", newTitle);
        return new PageBuilder(this.code);
    }
}
