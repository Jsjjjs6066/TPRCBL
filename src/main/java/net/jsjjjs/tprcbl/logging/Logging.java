package net.jsjjjs.tprcbl.logging;

import org.fusesource.jansi.Ansi;
import org.jetbrains.annotations.NotNull;

public class Logging {
    public void log(@NotNull String prefix, Ansi.Color color, Object object) {
        if (color != null) {
            System.out.println(Ansi.ansi().fg(color).a(prefix).a(object).fg(Ansi.Color.DEFAULT));
        }
    }
}
