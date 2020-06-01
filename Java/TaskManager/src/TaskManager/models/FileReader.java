package TaskManager.models;

import TaskManager.models.task.Task;

import java.util.List;

public interface FileReader {
    List<Task> read(String filename);
    List<Integer> getLastResources();
}
