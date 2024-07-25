package net.jsjjjs.tprcbl.logging;

import org.fusesource.jansi.Ansi;
import org.jetbrains.annotations.NotNull;

import java.util.Objects;

public class Logging {
    public void log(Ansi.Color color, Object object) {
        System.out.println(Ansi.ansi().fg(Objects.requireNonNullElse(color, Ansi.Color.DEFAULT)).a(object).fg(Ansi.Color.DEFAULT));
    }


}
