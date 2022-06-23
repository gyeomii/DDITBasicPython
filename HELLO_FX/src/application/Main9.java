package application;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

public class Main9 extends Application {
	Parent root;
	Scene scene;
	Button btn1;
	Button btn2;
	Button btn3;
	Button btn4;
	Button btn5;
	Button btn6;
	Button btn7;
	Button btn8;
	Button btn9;
	Button btn0;
	Button call;
	TextField tf;


	@Override
	public void start(Stage primaryStage) {
		try {
			root = FXMLLoader.load(getClass().getResource("main9.fxml"));
			scene = new Scene(root, 300, 500); // (width, height)
			btn1 = (Button) scene.lookup("#btn1");
			btn2 = (Button) scene.lookup("#btn2");
			btn3 = (Button) scene.lookup("#btn3");
			btn4 = (Button) scene.lookup("#btn4");
			btn5 = (Button) scene.lookup("#btn5");
			btn6 = (Button) scene.lookup("#btn6");
			btn7 = (Button) scene.lookup("#btn7");
			btn8 = (Button) scene.lookup("#btn8");
			btn9 = (Button) scene.lookup("#btn9");
			btn0 = (Button) scene.lookup("#btn0");
			call = (Button) scene.lookup("#btnCall");
			tf = (TextField) scene.lookup("#tf");
			
			btn1.setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {input(event);}});
			btn2.setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {input(event);}});
			btn3.setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {input(event);}});
			btn4.setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {input(event);}});
			btn5.setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {input(event);}});
			btn6.setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {input(event);}});
			btn7.setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {input(event);}});
			btn8.setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {input(event);}});
			btn9.setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {input(event);}});
			btn0.setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {input(event);}});

			call.setOnMouseClicked(new EventHandler<Event>() {public void handle(Event event) {calling();}});
			
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public void input(Event event){ 
		Button temp = (Button) event.getSource(); 
		tf.appendText(temp.getText()); 
		}
	
	public void calling() {
		Alert alert = new Alert(AlertType.INFORMATION);
		alert.setTitle("Calling...");
		alert.setHeaderText("Calling to " + tf.getText());
		alert.setContentText("Please Wait to Connect");
		alert.show();
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}