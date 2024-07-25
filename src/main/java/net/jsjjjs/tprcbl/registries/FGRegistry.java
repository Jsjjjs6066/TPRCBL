package net.jsjjjs.tprcbl.registries;

public enum FGRegistry {
    RESET("\u001B[0m"),
    RED("\u001B[31m"),
    GREEN("\u001B[32m"),
    YELLOW("\u001B[33m");

    private final String chars;

    FGRegistry(String chars) {
        this.chars = chars;
    }

    public String color() {
        return this.chars;
    }
}
