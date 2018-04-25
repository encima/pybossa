/**
 * Pybossa API
 * API for the Pybossa project
 *
 * OpenAPI spec version: 0.0.1
 * Contact: support@scifabric.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import io.swagger.annotations.*;
import com.google.gson.annotations.SerializedName;

@ApiModel(description = "")
public class TaskId {
  
  @SerializedName("task_id")
  private Integer taskId = null;

  /**
   **/
  @ApiModelProperty(required = true, value = "")
  public Integer getTaskId() {
    return taskId;
  }
  public void setTaskId(Integer taskId) {
    this.taskId = taskId;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TaskId taskId = (TaskId) o;
    return (this.taskId == null ? taskId.taskId == null : this.taskId.equals(taskId.taskId));
  }

  @Override
  public int hashCode() {
    int result = 17;
    result = 31 * result + (this.taskId == null ? 0: this.taskId.hashCode());
    return result;
  }

  @Override
  public String toString()  {
    StringBuilder sb = new StringBuilder();
    sb.append("class TaskId {\n");
    
    sb.append("  taskId: ").append(taskId).append("\n");
    sb.append("}\n");
    return sb.toString();
  }
}
